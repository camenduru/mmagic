_base_ = './base_glean.py'

experiment_name = 'glean_ffhq_16x'
work_dir = f'./work_dirs/{experiment_name}'

scale = 16
# model settings
model = dict(
    type='SRGAN',
    generator=dict(
        type='GLEANStyleGANv2',
        in_size=64,
        out_size=1024,
        style_channels=512,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='http://download.openmmlab.com/mmgen/stylegan2/'
            'official_weights/stylegan2-ffhq-config-f-official_20210327'
            '_171224-bce9310c.pth',
            prefix='generator_ema')),
    discriminator=dict(
        type='StyleGAN2Discriminator',
        in_size=1024,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='http://download.openmmlab.com/mmgen/stylegan2/'
            'official_weights/stylegan2-ffhq-config-f-official_20210327'
            '_171224-bce9310c.pth',
            prefix='discriminator')),
    pixel_loss=dict(type='MSELoss', loss_weight=1.0, reduction='mean'),
    perceptual_loss=dict(
        type='PerceptualLoss',
        layer_weights={'21': 1.0},
        vgg_type='vgg16',
        perceptual_weight=1e-2,
        style_weight=0,
        norm_img=False,
        criterion='mse',
        pretrained='torchvision://vgg16'),
    gan_loss=dict(
        type='GANLoss',
        gan_type='vanilla',
        loss_weight=1e-2,
        real_label_val=1.0,
        fake_label_val=0),
    train_cfg=dict(),
    test_cfg=dict(),
    data_preprocessor=dict(
        type='EditDataPreprocessor',
        mean=[127.5, 127.5, 127.5],
        std=[127.5, 127.5, 127.5],
    ),
)

train_pipeline = [
    dict(type='LoadImageFromFile', key='img'),
    dict(type='LoadImageFromFile', key='gt'),
    dict(
        type='Flip',
        keys=['img', 'gt'],
        flip_ratio=0.5,
        direction='horizontal'),
    dict(type='ToTensor', keys=['img', 'gt']),
    dict(type='PackEditInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile', key='img'),
    dict(type='LoadImageFromFile', key='gt'),
    dict(type='ToTensor', keys=['img', 'gt']),
    dict(type='PackEditInputs')
]

# dataset settings
dataset_type = 'BasicImageDataset'

train_dataloader = dict(
    num_workers=8,
    batch_size=8,
    persistent_workers=False,
    sampler=dict(type='InfiniteSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(dataset_type='ffhq', task_name='sisr'),
        data_root='data/FFHQ',
        data_prefix=dict(img='BIx16_down', gt='GT'),
        ann_file='meta_info_FFHQ_GT.txt',
        pipeline=train_pipeline))

val_dataloader = dict(
    num_workers=8,
    persistent_workers=False,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(dataset_type='ffhq', task_name='sisr'),
        data_root='data/CelebA-HQ',
        data_prefix=dict(img='BIx16_down', gt='GT'),
        ann_file='meta_info_CelebAHQ_val100_GT.txt',
        pipeline=test_pipeline))

test_dataloader = val_dataloader