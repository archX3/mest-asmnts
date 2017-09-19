class Marker:
    def __init__(self, color = "Red"):
        self.color = color


class MarkerBox:
    def __init__(self, markers = []):
        self.markers = markers

    def add_marker(self, marker):
        self.markers.append(marker)

    def remove_marker(self, color):
        for marker in self.markers:
            if marker.color == color:
                self.markers.remove(marker)
                return marker
        return None

if __name__ == "__main__":
    mestMarkers = MarkerBox()

    mestMarkers.add_marker(Marker(color = "blue"))
    mestMarkers.add_marker(Marker(color = "black"))
    mestMarkers.remove_marker(color = "blue")

    # mstmrkrs = mestMarkers.markers

    for marker in mestMarkers.markers:
        print(marker.color)

    print("number of markers = ", len(mestMarkers.markers))

