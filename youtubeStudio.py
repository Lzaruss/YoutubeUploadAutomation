import pyautogui

howManyVideos=5

def goToImage(nombre):
    ubi = pyautogui.locateOnScreen(nombre, confidence=0.8)
    if ubi is not None:
        coordenadas = pyautogui.center(ubi)
        return coordenadas.x, coordenadas.y
    else:
        return None, None


def cambiarVideo():
    # Lógica para cambiar el video
    pyautogui.click()
    pyautogui.sleep(2)

    x, y = goToImage("youtubeStudioImg/visibilidad.PNG")
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.sleep(2)

    pyautogui.click()
    #Publicar el video
    x, y = goToImage("youtubeStudioImg/publicar.PNG")
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.sleep(2)

    pyautogui.click()
    pyautogui.sleep(4)
    #Cerrar el video
    x, y = goToImage("youtubeStudioImg/cerrarVideo.PNG")
    pyautogui.moveTo(x, y)
    pyautogui.sleep(2)

    pyautogui.click()

if __name__ == '__main__':
    # Comprobar si la imagen "youtube.png" está en pantalla
    youtube_img = pyautogui.locateOnScreen("youtubeStudioImg/youtubeStudio.png")
    if youtube_img is not None:
        for imagen in range(howManyVideos):
            ubicacion = pyautogui.locateOnScreen("youtubeStudioImg/editarBorrador.PNG", confidence=0.8)
            if ubicacion is not None:
                x, y = goToImage("youtubeStudioImg/editarBorrador.PNG")
                pyautogui.moveTo(x, y, duration=0.5)
                cambiarVideo()
                pyautogui.sleep(2)
            else:
                pyautogui.scroll(-100)