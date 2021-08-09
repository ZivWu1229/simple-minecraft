from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

paused = False
texture = {}
block_taking = 2

app = Ursina()

texture[1] = load_texture('assets/dirt.png')
texture[2] = load_texture('assets/stone.png')
texture[3] = load_texture('assets/oak_planks.png')
texture[4] = load_texture('assets/oak_log.png')

def update():
	global block_taking
	global paused
	block.texture = texture[block_taking]
	if held_keys['1']:
		block_taking = 1
	if held_keys['2']:
		block_taking = 2
	if held_keys['3']:
		block_taking = 3
	if held_keys['4']:
		block_taking = 4

class Voxel(Button):
	"""docstring for Voxel"""
	def __init__(self,position = (0,0,0),block = 2):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = texture[block],
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.white
			)
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				voxel = Voxel(position = self.position + mouse.normal,block = block_taking)
			if key == 'left mouse down':
				destroy(self)

class Block(Entity):
	"""docstring for Bolck"""
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'cube',
			position = Vec3(0.7,-0.4,0),
			texture = texture[block_taking],
			scale = 0.5,
			rotation = 22.5
			)	
block = Block()

for z in range(20):
	for x in range(20):
		voxel = Voxel(position = (x,0,z))
player = FirstPersonController()
app.run()
