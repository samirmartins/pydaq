from moviepy.editor import VideoFileClip

# Carregar o vídeo
clip = VideoFileClip("entrada.mp4")

# (Opcional) Definir um trecho específico do vídeo
# clip = clip.subclip(5, 10)  # do segundo 5 ao 10

# (Opcional) Redimensionar para reduzir o tamanho do GIF
# clip = clip.resize(0.5)

# Exportar como GIF
clip.write_gif("saida.gif")
