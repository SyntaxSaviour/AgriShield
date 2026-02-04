<<<<<<< HEAD
import os
import shutil
import random

# Set seed for reproducibility
random.seed(42)

# Paths
base_dir = "data"
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")
test_dir = os.path.join(base_dir, "test")

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create val and test directories
for split_dir in [val_dir, test_dir]:
    os.makedirs(split_dir, exist_ok=True)

# Process each class folder
for class_name in os.listdir(train_dir):
    class_path = os.path.join(train_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    total = len(images)
    train_end = int(train_ratio * total)
    val_end = train_end + int(val_ratio * total)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    # Create class folders in val and test
    os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Move images
    for img in val_images:
        shutil.move(
            os.path.join(class_path, img),
            os.path.join(val_dir, class_name, img)
        )

    for img in test_images:
        shutil.move(
            os.path.join(class_path, img),
            os.path.join(test_dir, class_name, img)
        )

    print(f"{class_name}: "
          f"Train={len(train_images)}, "
          f"Val={len(val_images)}, "
          f"Test={len(test_images)}")

print("Dataset splitting completed.")
=======
import os
import shutil
import random

# Set seed for reproducibility
random.seed(42)

# Paths
base_dir = "data"
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")
test_dir = os.path.join(base_dir, "test")

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create val and test directories
for split_dir in [val_dir, test_dir]:
    os.makedirs(split_dir, exist_ok=True)

# Process each class folder
for class_name in os.listdir(train_dir):
    class_path = os.path.join(train_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    total = len(images)
    train_end = int(train_ratio * total)
    val_end = train_end + int(val_ratio * total)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    # Create class folders in val and test
    os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Move images
    for img in val_images:
        shutil.move(
            os.path.join(class_path, img),
            os.path.join(val_dir, class_name, img)
        )

    for img in test_images:
        shutil.move(
            os.path.join(class_path, img),
            os.path.join(test_dir, class_name, img)
        )

    print(f"{class_name}: "
          f"Train={len(train_images)}, "
          f"Val={len(val_images)}, "
          f"Test={len(test_images)}")

print("Dataset splitting completed.")
>>>>>>> 6ecde937352cf0bd7f39dcbdbc851741a25eb044
