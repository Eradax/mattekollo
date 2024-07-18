from datetime import datetime
import atexit

import torch
import torchvision

import test_ai

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_model():
    class Model(torch.nn.Module):
        def __init__(self):
            super().__init__()
    
            self.stack = torch.nn.Sequential(
            torch.nn.Linear(28*28, 800),
            torch.nn.ReLU(),
            torch.nn.Linear(800, 10),
            )
        
        def forward(self, x):
            ret = self.stack(x)

            return ret
    
    model = Model()

    return model

def get_optimizer():
    optimizer = torch.optim.SGD(model.parameters())
    
    return optimizer

def get_loss_fn():
    loss_fn = torch.nn.CrossEntropyLoss()

    return loss_fn

def calculate_loss(output, target, loss_fn):
    r_target = torch.zeros(10).to(device)
    r_target[target] = 1

    loss = loss_fn(output, r_target)
    loss.backward()

    return loss

def preprocess_img(image_data):
    ret = torch.flatten(image_data.to(device)) / 255
    
    return ret


def main():
    image_directory = "images/"
    training_set = torchvision.datasets.MNIST(
            image_directory,
            download = True,
            train = True,
            transform = torchvision.transforms.ToTensor()
    )

    training_data = torch.utils.data.DataLoader(
        training_set,
        batch_size = 2**0,
        shuffle = True,
        num_workers = 0,
    )

    test_set = torchvision.datasets.MNIST(
            image_directory,
            download = True,
            train = False,
            transform = torchvision.transforms.ToTensor()
    )

    test_data = torch.utils.data.DataLoader(
        test_set,
        batch_size = 2**0,
        shuffle = True,
        num_workers = 0,

    )

    global model
    model = get_model().to(device)
    atexit.register(save_model)

    optimizer = get_optimizer()
    loss_fn = get_loss_fn()
       
    epochs = 1000
    for epoch in range(1, epochs+1):
        for batch_idx, (image_data, target) in enumerate(training_data, start=1):
            image_data = preprocess_img(image_data).to(device)

            optimizer.zero_grad()
            output = model(image_data).to(device)
            loss = calculate_loss(output, target, loss_fn)
            optimizer.step()

            if batch_idx % 100 == 0:
                print(f"{batch_idx = }")
        
        right, wrong, total = test_ai.check(model, test_data)
    
        print(f"{epoch = } avg: {right/total:.2%}")
        if epoch % 10 == 0:
            save_model()
    
def save_model():
    model_path = f"models/mnist_model_{datetime.now():%m%d:%H%M}.pth"
    torch.save(model.state_dict(), model_path)

if __name__ == "__main__":
    main()
