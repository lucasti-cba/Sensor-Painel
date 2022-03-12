# -*- coding: utf-8 -*-
import sys
import os
import time
import pygame
from bin.config import *
from datetime import datetime
import psutil
import plotly.graph_objects as go
import numpy as np
from image import *
np.random.seed(1)
from PIL import Image


size=(1080,920)
FORMAT = "RGBA"


def pil_to_game(img):
    data = img.tobytes("raw", FORMAT)
    return pygame.image.fromstring(data, img.size, FORMAT)

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert(FORMAT)


def renderQuerry(querry, font_size, cor, screen, position):
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte, font_size)
	txttela = fontesys.render(querry, 1, cor)
	return screen.blit(txttela,position)

def start_the_game():
	pygame.init()
	global tela
	infoObject = pygame.display.Info()
	tela = pygame.display.set_mode((infoObject.current_w-10, infoObject.current_h-10), pygame.SHOWN|pygame.RESIZABLE, 0)
	pygame.display.set_caption('Sensor Monitor Information ')
	clock = pygame.time.Clock()

	
	# img = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/bin/img/wpp2.jpg')
	clock.tick(60)
	key=pygame.key.get_pressed()  #checking pressed keys
	done = False
	gif_img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/image/bg.gif')
	gif_img2 = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/image/bg2.gif')
	current_frame = 0
	conttime = 0
	while not done:
    	#events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

				
	### PAINEL PADRAO
		
		data_e_hora_atuais = datetime.now()
		mes = ['janeiro', 'fevereiro', 'março' , 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
		data = data_e_hora_atuais.strftime(', %d de '+mes[data_e_hora_atuais.month - 1 ]+' de %Y')
		hora = data_e_hora_atuais.strftime('%H:%M:%S')
		tela.fill(cor['verde1'])
		draw1 = pygame.draw.rect(tela, cor['verde1'], [0, 0, infoObject.current_w, infoObject.current_h])
		#renderQuerry(str(usage_cpu), 36, cor['verde2'], tela, [50,20] )		
		bloco = pygame.draw.rect(tela, cor['branco'], [0, 0, 150, 120])
		bloco2 = pygame.draw.rect(tela, cor['branco'], [152, 0, 150, 120])
		draw1
	
		frame = pil_to_game(get_gif_frame(gif_img, current_frame))
		frame2 = pil_to_game(get_gif_frame(gif_img2, current_frame))
		###MEMORIAS
		renderQuerry('Memória', 36, cor['verde2'], tela, [10,10] )
		renderQuerry('Em uso:', 24, cor['verde2'], tela, [10,40] )
		renderQuerry(str(psutil.virtual_memory()[2]) + " %", 24, cor['verde2'], tela, [80,40] )
		renderQuerry('Total:', 24, cor['verde2'], tela, [10,60] )
		renderQuerry( str("%.2f" % (psutil.virtual_memory()[0]/1073741824))+' Gb' , 24, cor['verde2'], tela, [60,60] )
		renderQuerry('Livre:', 24, cor['verde2'], tela, [10,100] )
		renderQuerry( str("%.2f" % (psutil.virtual_memory()[1]/1073741824))+' Gb' , 24, cor['verde2'], tela, [60,100] )
		##PROCESSADOR
		renderQuerry('Processador', 36, cor['verde2'], tela, [154,10] )
		renderQuerry('Em uso:', 24, cor['verde2'], tela, [154,40] )
		renderQuerry(str(psutil.cpu_percent(interval=0.05)) + " %", 24, cor['verde2'], tela, [240,40] )
		renderQuerry('Clock:', 24, cor['verde2'], tela, [154,60] )
		renderQuerry( str("%.2f" % (psutil.cpu_freq()[2]/1024))+' GHz' , 24, cor['verde2'], tela, [210,60] )
		renderQuerry('Livre:', 24, cor['verde2'], tela, [154,100] )
		renderQuerry( str( (psutil.cpu_percent(interval=0.05 , percpu= True)))+' GHz' , 24, cor['verde2'], tela, [200,100] )


		tela.blit(frame, (0, 122))
		tela.blit(frame2, (0, 500))
		conttime = conttime + 1
		# if conttime == 10:
		current_frame = (current_frame + 1) % gif_img.n_frames
		conttime = 0
		# lista = getdados()
		# lista = bubbleSort(lista)
		inicioy = 156
		cli = 0
		cir = 0
		livre = 0
		count_cpu = psutil.cpu_count()
		usage_cpu = psutil.virtual_memory()
		inicioy = 156
		# for row in lista:
		# 	inicio = [(0,inicioy),(infoObject.current_w + 1000, 20 )]
		# 	renderAlas(row, tela, 'VERDE', inicio , inicioy+4)

		# 	inicioy += 22
		
		# renderQuerry(str(cir), 36, cor['verde2'], tela, [1200,60] )	
		pygame.display.update()
		pygame.display.flip()
	pygame.quit()

# while True:
# 	try:
# 		start_the_game()
# 	except:
# 		print('error')
# 		start_the_game()
start_the_game()