import matplotlib.pyplot as plt
import io
import base64
 
def build_graph(ts):
    img = io.BytesIO()
    plt.plot(ts)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)