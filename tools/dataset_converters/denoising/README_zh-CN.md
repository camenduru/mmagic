# 准备 Denoising 数据集

<!-- [DATASET] -->

```bibtex
@inproceedings{Zamir2021Restormer,
  title={Restormer: Efficient Transformer for High-Resolution Image Restoration},
  author={Syed Waqas Zamir and Aditya Arora and Salman Khan and Munawar Hayat and Fahad Shahbaz Khan and Ming-Hsuan Yang},
  booktitle={CVPR},
  year={2022}
}
```

测试数据集(Set12, BSD68, CBSD68, Kodak, McMaster, Urban100)可以从 [此处](https://drive.google.com/file/d/1P_-RAvltEoEhfT-9GrWRdpEi6NSswTs8/) 下载。

文件目录结构应如下所示：

```text
mmediting
├── mmedit
├── tools
├── configs
├── data
|   ├── denoising_gaussian_test
|   |   ├── Set12
|   |   ├── BSD68
|   |   ├── CBSD68
|   |   ├── Kodak
|   |   ├── McMaster
|   |   ├── Urban100
```