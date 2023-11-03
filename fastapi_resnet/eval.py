import io
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image


class MyNet():
    def __init__(self) -> None:
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)

    def predict(self, image):
        self.model.eval()
        if type(image) == str:
            img = Image.open(image).convert('RGB')
        else:
            img = Image.open(io.BytesIO(image)).convert('RGB')

        preprocess = self.weights.transforms()

        batch = preprocess(img).unsqueeze(0)

        prediction = self.model(batch).squeeze(0).softmax(0)
        class_id = prediction.argmax().item()
        score = prediction[class_id].item()
        category_name = self.weights.meta["categories"][class_id]

        return f"{category_name}: {round(score*100, 2)}%"


if __name__ == "__main__":
    my_net = MyNet()
    print(my_net.predict("tig.png"))
