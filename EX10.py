"""Mandelbrot set and Julia set."""

from PIL import Image
import math
import colorsys


class Fractal:
    """Fractal class."""

    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        self.size = size
        self.scale = scale
        self.computation = computation
        self.img = Image.new("RGBA", (size[0], size[1]))

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                i = self.pixel_value((x, y))[0]
                # x_scaled, y_scaled = self.pixel_value((x, y))[1], self.pixel_value((x, y))[2]
                # z = self.computation((x_scaled, y_scaled))[1]
                # smooth = i + 1 - math.log(math.log(abs(z))) / math.log(2)
                #smooth = smooth / 500
                quotient = i / 1000
                color = int(max(0.0, min(quotient, 1.0)) * 255.999)

                if quotient > 0.5:
                    self.img.putpixel((x, y), (color, 255, color))
                else:
                    self.img.putpixel((x, y), (0, color, 0))

                #print(colortuple)
                #print(colortuple)
                #rgb = colorsys.hsv_to_rgb(color,)
                #print(rgb)
                #self.img.putpixel((x, y), rgb)
                #print(smooth)
                #print(smooth)

                #print(rgb)
                #print(smooth -2 )
                #self.img.putpixel((x, y), None)
                #print(color)
                #color = color / 1000 * 255
                #color = log(i + 1.5 - log(log(abs(sqrt(x_scaled ** 2 + y_scaled ** 2))), 2)) / 3.4
                # g = int((color ** 2.5) / 255 * 255.999)
                # b = int(color / 255 * 255.999)


    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        # x = pixel[0] * (self.scale[1][0] - self.scale[0][0]) / self.size[0] + self.scale[0][0]
        # y = pixel[1] * (self.scale[1][1] - self.scale[0][1]) / self.size[1] + self.scale[0][1]
        x_scaled = (pixel[0] / self.size[0]) * (self.scale[1][0] - self.scale[0][0]) + self.scale[0][0]
        y_scaled = (pixel[1] / self.size[1]) * (self.scale[1][1] - self.scale[0][1]) + self.scale[0][1]

        return self.computation((x_scaled, y_scaled))[0], x_scaled, y_scaled

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        self.img.save(filename, "PNG")

if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        """Return integer -> how many iterations it takes for the pixel to escape the mandelbrot set."""
        c = complex(pixel[0], pixel[1])  # Complex number: A + Bi  (A is real number, B is imaginary number).
        z = 0  # We are assuming the starting z value for each square is 0.
        iterations = 0  # Will count how many iterations it takes for a pixel to escape the mandelbrot set.

        for i in range(1000):  # The more iterations, the more detailed the mandelbrot set will be.
            if abs(z) >= 2.0:  # Checks, if pixel escapes the mandelbrot set. Same as square root of pix[0] and pix[1].
                break
            z = z**2 + c
            iterations += 1

        return iterations, z


    def julia_computation(pixel):
        """Return integer -> how many iterations it takes for the pixel to escape the mandelbrot set."""
        c = complex(-0.1, 0.651)
        z = complex(pixel[0], pixel[1])
        iterations = 0  # Will count how many iterations it takes for a pixel to escape the mandelbrot set.

        for i in range(255):  # The more iterations, the more detailed the mandelbrot set will be.
            if abs(z) >= 2.0:  # Checks, if pixel escapes the mandelbrot set. Same as square root of pix[0] and pix[1].
                break
            z = z**2 + c
            iterations += 1

        return iterations, z

    mandelbrot6 = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot6.compute()
    mandelbrot6.save_image("LASTTEST.png")


        # mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], julia_computation)
    # mandelbrot.compute()
    # mandelbrot.save_image("mandelbrot.png")
    # mandelbrot2 = Fractal((250, 250), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    # mandelbrot2.compute()
    # mandelbrot2.save_image("testsmooth2.png")
    # #
    # mandelbrot1 = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    # mandelbrot1.compute()
    # mandelbrot1.save_image("test1.png")
    #
    # mandelbrot2 = Fractal((1000, 1000), [(-1.5, -1.5), (1.5, 1.5)], mandelbrot_computation)
    # mandelbrot2.compute()
    # mandelbrot2.save_image("test2.png")
    #
    # mandelbrot3 = Fractal((1000, 1000), [(-1, -1), (1, 1)], mandelbrot_computation)
    # mandelbrot3.compute()
    # mandelbrot3.save_image("test3.png")
    #
    # mandelbrot4 = Fractal((1000, 1000), [(-0.5, -0.5), (0.5, 0.5)], mandelbrot_computation)
    # mandelbrot4.compute()
    # mandelbrot4.save_image("test4.png")
    #
    # mandelbrot5 = Fractal((1000, 1000), [(-0.3, -0.3), (0.3, 0.3)], mandelbrot_computation)
    # mandelbrot5.compute()
    # mandelbrot5.save_image("test5.png")
