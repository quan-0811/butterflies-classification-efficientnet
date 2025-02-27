import torchvision
from torch.utils.data import DataLoader
from module.augmented_dataset import AugmentedDataset

def create_dataloaders(train_dir: str, valid_dir: str, test_dir: str, batch_size: int, transform, augmented_transforms):

    train_dataset = AugmentedDataset(root=train_dir, transform=transform, aug_transforms=augmented_transforms)
    valid_dataset = torchvision.datasets.ImageFolder(root=valid_dir,
                                                    transform=transform)
    test_dataset = torchvision.datasets.ImageFolder(root=test_dir,
                                                    transform=transform)

    train_dataloader = DataLoader(dataset=train_dataset,
                                  batch_size=batch_size,
                                  shuffle=True,
                                  pin_memory=True)
    valid_dataloader = DataLoader(dataset=valid_dataset,
                                  batch_size=batch_size,
                                  shuffle=False,
                                  pin_memory=True)
    test_dataloader = DataLoader(dataset=test_dataset,
                                 batch_size=batch_size,
                                 shuffle=False,
                                 pin_memory=True)

    return train_dataloader, valid_dataloader, test_dataloader, valid_dataset.classes