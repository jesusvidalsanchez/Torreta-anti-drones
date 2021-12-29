import cv2
import sys

class detector_Drones:

    def __init__(self):
        # Constructor de clase
        self.path_weights = sys.path[0] + "{\\path relativo weights}"
        self.path_config  = sys.path[0] + "{\\path relativo config}"
        self.net = cv2.dnn.readNet(self.path_weights,self.path_config)

    def detectarDrones(self, img):
        # Función de busqueda y localización de drones en la imagen proporcionada
        drone_class = ['drone']