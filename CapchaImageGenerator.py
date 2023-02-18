from PIL import Image, ImageFont, ImageDraw 

class CapchaImageGenerator:
    """A class for generating image of the nick on a neon background"""    
    @staticmethod
    def generate_image(nick: str) -> Image:
        """Function that returns image of the nick on a neon background

        Args:
            nick (str): the nick

        Returns:
            Image: the final image
        """        
        image_size_x = 768
        image_size_y = 720
        
        my_image = Image.new('1', (768, 720), 'white')
        image_editable = ImageDraw.Draw(my_image)
        
        title_font = ImageFont.truetype('Karlocham-Brush.otf', 150)
        text_width, text_height = image_editable.textbbox((0, 0), text=nick, font=title_font)[2:4]
        
        if image_editable.textbbox((0, 0), text=nick, font=title_font)[2] > image_size_x:
            i = 150
            while text_width > image_size_x:
                title_font = ImageFont.truetype('Karlocham-Brush.otf', i)
                text_width = image_editable.textbbox((0, 0), text=nick, font=title_font)[2]
                i -= 1

        image_editable.text(xy=((image_size_x - text_width)/2, (image_size_y - text_height)/2), text=nick, align="center", font=title_font)

        return my_image