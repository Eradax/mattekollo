import torch
import torchvision

def check(model, test_data) -> tuple[int]:
    right = 0
    wrong = 0
    total = 0
    
    for image_data, target in test_data:
        image_data = torch.flatten(image_data) / 255
        output = model(image_data)
    
        argmax = torch.argmax(output)
    
        total += 1
        if argmax.item() == target:
            right += 1
        else:
            wrong += 1

    assert total == right + wrong

    return right, wrong, total

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.forward_layer = torch.nn.Linear(28**2, 10)

    def forward(self, x):
        return self.forward_layer(x)

def main():
    image_directory = "images/"
    test_data = torchvision.datasets.MNIST(image_directory,
            download = True,
            train = False,
            transform = torchvision.transforms.ToTensor()
    )
    
    
    model = Model()
    
    model_path = "./model/mnist_model_current.pth"
    model.load_state_dict(torch.load(model_path))
    model.eval()
    
    right, wrong, total = check(model, test_data)

    print(f"{right = }")
    print(f"{wrong = }")
    print(f"{total = }")
    
    print(f"precentage right: {right/total:.2%}")

if __name__ == "__main__":
    main()
