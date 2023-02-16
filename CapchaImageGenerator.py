from PIL import Image, ImageFont, ImageDraw 

class CapchaImageGenerator:
    """A class for generating image of the nick on a neon backgtound"""    
    @staticmethod
    def generate_image(nick: str) -> Image:
        """Function that returns image of the nick on a neon backgtound

        Args:
            nick (str): the nick

        Returns:
            Image: the final image
        """        
        image_size_x = 768
        image_size_y = 720

        my_image = Image.new('1', (768, 720), 'white')
        title_font = ImageFont.truetype('Karlocham-Brush.otf', 150)

        image_editable = ImageDraw.Draw(my_image)
        _, _, text_width, text_height = image_editable.textbbox((0, 0), nick, font=title_font)

        image_editable.text(xy=((image_size_x - text_width)/2, (image_size_y - text_height)/2), text=nick, align="center", font=title_font)

        return my_image