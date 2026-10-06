import sys
from fontTools.ttLib import TTFont
from fontTools.pens.basePen import BasePen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

CLAY, INK, CHALK = "%23cc6633", "%23141414", "%23f0e0d0"  # "%23" is "#" in a data URI
BOX, LETTER, WIDTH = 64, 44, 38  # max letter height and width; wide capitals shrink to fit


class Centroid(BasePen):
    """Area-weighted centroid of a glyph; counters subtract because their winding is opposite."""

    def __init__(self, glyphs):
        super().__init__(glyphs)
        self.area = self.cx = self.cy = 0
        self.start = self.last = None

    def edge(self, a, b):
        cross = a[0] * b[1] - b[0] * a[1]
        self.area += cross / 2
        self.cx += (a[0] + b[0]) * cross / 6
        self.cy += (a[1] + b[1]) * cross / 6

    def _moveTo(self, p):
        self.start = self.last = p

    def _lineTo(self, p):
        self.edge(self.last, p)
        self.last = p

    def _curveToOne(self, p1, p2, p3):
        a = self.last
        for i in range(1, 9):
            t = i / 8
            u = 1 - t
            self._lineTo(tuple(u**3 * a[k] + 3 * u * u * t * p1[k] + 3 * u * t * t * p2[k] + t**3 * p3[k] for k in (0, 1)))

    def _qCurveToOne(self, p1, p2):
        a = self.last
        for i in range(1, 9):
            t = i / 8
            u = 1 - t
            self._lineTo(tuple(u * u * a[k] + 2 * u * t * p1[k] + t * t * p2[k] for k in (0, 1)))

    def _closePath(self):
        self._lineTo(self.start)

    def center(self):
        return self.cx / self.area, self.cy / self.area


def favicon(font_path, char):
    font = TTFont(font_path)
    glyphs = font.getGlyphSet()
    glyph = glyphs[font.getBestCmap()[ord(char)]]
    bounds = BoundsPen(glyphs)
    glyph.draw(bounds)
    x0, y0, x1, y1 = bounds.bounds
    mass = Centroid(glyphs)
    glyph.draw(mass)
    mx, my = mass.center()
    s = min(LETTER / (y1 - y0), WIDTH / (x1 - x0))
    dx = BOX / 2 - s * (x0 + x1) / 2 + s * ((x0 + x1) / 2 - mx) / 2  # halfway from bbox center toward mass center
    dy = BOX / 2 + s * (y0 + y1) / 2 - s * ((y0 + y1) / 2 - my) / 2  # y flips: font y-up, svg y-down
    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    glyph.draw(TransformPen(pen, (s, 0, 0, -s, dx, dy)))
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           f"<rect width='64' height='64' rx='10' fill='{CLAY}'/>"
           f"<rect x='5' y='5' width='54' height='54' rx='4' fill='{INK}'/>"
           f"<path d='{pen.getCommands()}' fill='{CHALK}'/></svg>")
    return f'<link rel="icon" href="data:image/svg+xml,{svg}">'


if __name__ == "__main__":
    print(favicon(sys.argv[1], sys.argv[2].upper()))
