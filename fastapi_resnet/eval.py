import io
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image


# you can download the weights from here:
# https://download.pytorch.org/models/resnet50-11ad3fa6.pth
WEIGHTS_PATH = 'resnet50-11ad3fa6.pth'
# and the class labels from here:
# https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
CLASS_LABELS_PATH = 'class_labels.txt'


class ResNetInference:
    def __init__(self):
        self.weights_path = WEIGHTS_PATH
        self.class_labels_path = CLASS_LABELS_PATH
        self.class_labels = self._load_class_labels(self.class_labels_path)
        self.model = models.resnet50(pretrained=False)
        self._load_weights(self.weights_path)
        self.model.eval()

    def _load_weights(self, weights_path):
        checkpoint = torch.load(weights_path)
        self.model.load_state_dict(checkpoint)

    def _load_class_labels(self, class_labels_path):
        with open(class_labels_path) as f:
            class_labels = [line.strip() for line in f]
        return class_labels

    def preprocess_image(self, image):
        if type(image) == str:
            image = Image.open(image)
        else:
            image = Image.open(io.BytesIO(image))

        image = image.convert('RGB')

        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                                 0.229, 0.224, 0.225]),
        ])
        image = transform(image)
        image = image.unsqueeze(0)
        return image

    def inference(self, image):
        with torch.no_grad():
            output = self.model(image)
            probabilities = torch.nn.functional.softmax(output, dim=1)[0]
            predicted_class_index = torch.argmax(probabilities).item()
            predicted_class_label = self.class_labels[predicted_class_index]
            predicted_percentage = probabilities[predicted_class_index].item(
            ) * 100
            return {f'{predicted_class_label}: {round(predicted_percentage, 2)}'}


if __name__ == "__main__":
    my_net = ResNetInference()
    print(my_net.inference(my_net.preprocess_image("jaws.png")))
