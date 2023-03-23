# map_merge
---

This project's goal is merge 2 Visual-SfM model more faster than using Visual-SfM tools. If we have 274 images that contain 2 building, Visual-SfM takes 57.5minutes but if seperate 274 images to 136 images and 143 images it takes 13.1 minutes and 16.3 minutes each (no GPU). Code takes less than 1 minute.

---
### How to use
1. ready two Visual-SfM models, when making a model, each model must contains same images less than 15

----
일단 우리만 볼 수 있게 급하게라도 작성합니다...  
---
```bash
conda create -n py3-teaser python=3.6
conda activate py3-teaser
conda install scipy
pip install open3d
pip install numpy #아마 안해도 이미 설치 되어있을듯요
```
---
visual-sfm모델을 만드는데 15장 이상은 겹치도록 모델을 생성합니다  
후에 `.nvm`파일을 `.txt`로 변환해주고 main.py의 경로 설정을 바꿔줘요  
다음은 두 모델의 `.txt`파일에서 겹치는 이미지의 index를 찾아줘야하는데, 같은 이미지 이름 있는 줄 -4를 하면 그게 index에요  
그거를 `make_files.py`의 line 83, 114에 적용시켜줍니다.  
다음으로 겹치는 이미지중 하나를 골라서 해당하는 pose를 같은파일 39,40,42,43에 적용해줍니다.  
```python
python main.py
```
끝! 아직 코드 보완사항이 더 있어서 최종은 아니고... 그냥 지금까지 진행된거 공유 할 겸 한번 해보시라고 급하게나마 적어봅니다...  