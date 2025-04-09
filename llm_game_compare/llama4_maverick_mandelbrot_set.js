let xmin = -2.5;
let xmax = 1.5;
let ymin = -1.5;
let ymax = 1.5;
let maxIter = 100;

function setup() {
  createCanvas(800, 800);
  pixelDensity(1);
  colorMode(HSB, 360, 100, 100);
}

function draw() {
  background(0);
  loadPixels();
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      let c = mapToComplex(x, y);
      let m = mandelbrot(c, maxIter);
      let index = (x + y * width) * 4;
      if (m === maxIter) {
        pixels[index + 0] = 0; // black
        pixels[index + 1] = 0;
        pixels[index + 2] = 0;
        pixels[index + 3] = 255;
      } else {
        let hue = map(m, 0, maxIter, 0, 360);
        let c = color(hue, 100, 100);
        pixels[index + 0] = red(c);
        pixels[index + 1] = green(c);
        pixels[index + 2] = blue(c);
        pixels[index + 3] = 255;
      }
    }
  }
  updatePixels();
}

function mapToComplex(x, y) {
  let r = map(x, 0, width, xmin, xmax);
  let i = map(y, 0, height, ymin, ymax);
  return { r: r, i: i };
}

function mandelbrot(c, maxIter) {
  let z = { r: 0, i: 0 };
  for (let n = 0; n < maxIter; n++) {
    z = complexSquare(z);
    z = complexAdd(z, c);
    if (complexMag(z) > 2) {
      return n;
    }
  }
  return maxIter;
}

function complexSquare(z) {
  let r = z.r * z.r - z.i * z.i;
  let i = 2 * z.r * z.i;
  return { r: r, i: i };
}

function complexAdd(z1, z2) {
  let r = z1.r + z2.r;
  let i = z1.i + z2.i;
  return { r: r, i: i };
}

function complexMag(z) {
  return sqrt(z.r * z.r + z.i * z.i);
}

function mouseWheel(event) {
  let x = mouseX;
  let y = mouseY;
  let c = mapToComplex(x, y);
  let r = (xmax - xmin) / 4;
  xmin = c.r - r;
  xmax = c.r + r;
  let i = (ymax - ymin) / 4;
  ymin = c.i - i;
  ymax = c.i + i;
}

function mousePressed() {
  maxIter += 50;
}

function keyPressed() {
  if (key === '-') {
    maxIter -= 50;
    if (maxIter < 50) maxIter = 50;
  }
}