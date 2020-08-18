import numpy as np
from PIL import Image
from skimage.transform import resize
from torchvision import transforms

def distill(data, num_samples=100, width=6, height=6):
    idxs = np.random.random_integers(0, len(data) - 1, size=num_samples)
    sample = []
    for idx in idxs:
        sample.append(data[idx])

    dsample = np.zeros((num_samples, 3, width, height))

    process = transforms.Compose([transforms.Resize((width, height)), 
                                    transforms.ToTensor()])

    for i, img in enumerate(sample):
        dimg = np.asarray(process(img))
        dsample[i] = dimg

    distilled_data = np.zeros((2, 3, width, height))

    distilled_data[0] = np.mean(dsample, axis=0)
    distilled_data[1] = np.std(dsample, axis=0)

    return distilled_data
