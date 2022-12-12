import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64decode(image_png)
    graph = graph.decode('utf-8', errors = 'ignore')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Glucose Level')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Gl')
    plt.ylabel('Date')
    graph = get_graph()
    return graph
