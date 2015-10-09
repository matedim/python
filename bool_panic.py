# coding: utf8
# Паника мячей
# Игрок должен ловить мячи
from livewires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
	"""Перемещение руки"""
	image=games.load_image("hands_main.png")

	def __init__(self):
		"""Инициализация Рук и отображения счета"""
		super(Pan, self).__init__(image=Pan.image,
									x=games.mouse.x,
									bottom=games.screen.height)
		self.score=games.Text(value=0,size=45,color=color.black,
									top=5, right=games.screen.width-10)
		games.screen.add(self.score)

	def update(self):
		"""Перемещает обьект в по горизонтали"""
		self.x=games.mouse.x
		if self.left<0:
			self.left=0
		if self.right>games.screen.width:
			self.right=games.screen.width
		self.check_catch()
	def check_catch(self):
		"""Проверка словили ли мяч"""
		for bool in self.overlapping_sprites:
			self.score.value+=10
			self.score.right=games.screen.width-10
			bool.handle_caught()

class Bool(games.Sprite):
	"""Мячи падающие на землю"""
	image=games.load_image("myach2.png")
	speed=1

	def __init__(self, x, y=90):
		"""Инициализация  обьекта мяч"""
		super(Bool, self).__init__(image=Bool.image,
									x=x, y=y,
									dy=Bool.speed)
	def update(self):
		"""Проверка не коснулась ли границы экрана спрайт"""
		if self.bottom >games.screen.height:
			self.end_game()
			self.destroy()

	def handle_caught(self):
		"""Разрушает обьект пойманным игроком"""
		self.destroy()

	def end_game(self):
		"""Завершение игры"""
		end_message=games.Message(value="Game Over",
									size=90,
									color=color.red,
									x=games.screen.width/2,
									y=games.screen.height/2,
									lifetime=5*games.screen.fps,
									after_death=games.screen.quit)
		games.screen.add(end_message)
class Hero(games.Sprite):
	"""Герой который бросает мяч"""
	image=games.load_image("hero.png")

	def __init__(self, y=55, speed=2, adds_change=200):
		"""Инициализация  Героя"""
		super(Hero, self).__init__(image=Hero.image,
									x=games.screen.width/2,
									y=y,
									dx=speed)
		self.adds_change=adds_change
		self.time_til_drop=0

	def update(self):
		"""Определяет надо ли менять направление"""
		if self.left<0 or self.right>games.screen.width:
			self.dx=-self.dx
		elif random.randrange(self.adds_change)==0:
			self.dx=-self.dx
		self.check_drop()

	def check_drop(self):
		"""Уменьшение интервала ожидания и сбрасывание мяча"""
		if self.time_til_drop>0:
			self.time_til_drop -=1
		else:
			new_bool=Bool(x=self.x)
			games.screen.add(new_bool)
			self.time_til_drop=int(new_bool.height*1.3/Bool.speed)+1




def main():
	wall_image=games.load_image("wall21.jpg",transparent=False)
	games.screen.background=wall_image

	the_hero=Hero()
	games.screen.add(the_hero)

	the_pan=Pan()
	games.screen.add(the_pan)

	games.mouse.is_visible=False
	games.screen.event_grab=True


	games.screen.mainloop()

#start

main()
