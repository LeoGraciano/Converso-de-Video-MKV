import fnmatch
from importlib.resources import path
import sys
import os

if sys.platform == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    command_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_auto = '-b:a 320k'
# debug = '-ss 00:00:00 -to 00:00:10'
debug = ''

# path_origin = './video'
# path_destine = './convert'
# video_format_output = '.mp4'
path_origin = str(input('Qual Campinho dos aquivos ?'))
path_destine = str(input('Onde deseja Salvar?'))
video_format_output = '.'
video_format_output += str(input('Qual formato ?'))

for root, folders, files in os.walk(os.path.join(path_origin)):
    for file in files:
        if not fnmatch.fnmatch(file, "*.mkv"):
            continue

        path_complete = os.path.join(root, file)
        new_file, extension = os.path.splitext(file)
        path_legends = new_file + '.str'

        if os.path.isfile(path_legends):
            input_legends = f'-i "{path_legends}"'
            map_legends = '-c:s str -map: v:0 -map a -map 1:0'
        else:
            input_legends = ''
            map_legends = ''

        file_output = f'{path_destine}/{new_file}_new{video_format_output}'

        command = f'{command_ffmpeg} -i "{path_complete}" {input_legends} {codec_video} {crf} {preset} {codec_audio} {bitrate_auto} {debug} {map_legends} "{file_output}"'

        os.system(command)
