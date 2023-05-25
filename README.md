# Some Like It 90's

## 1. 팀원 정보 및 업무 분담 내역

저희 팀은 총 2명으로 구성되어 있습니다.

###### 안대현 (팀장)

- 영화 정보 제공 기능
- MBTI 기반 영화 추천 기능
- 위치 기반 영화관 정보 제공 기능
- 영화 관련 페이지

### 정진욱

- 회원가입 로그인, 팔로잉과 같은 유저 관련 기능
- 게시글 CRUD를 통한 커뮤니티 기능
- 유저와 커뮤니티 관련 페이지

## 2. 목표 서비스 구현 및 실제 구현 정도

저희 프로젝트의 목표는 영화와 관련된 다양한 정보를 제공하고 이것을 통해 사용자들간에 소통하는 장을 만드는 것입니다. 그래서 저희가 목표로 하는 서비스는 영화 정보 제공을 위한 서비스, 영화관 위치 정보 제공을 위한 서비스, 유저들간의 의견 및 정보 공유를 위한 커뮤니티 서비스를 구현하는 것입니다.

여기서 영화 정보 제공 서비스는 단순 정보 제공이 아닌 키워드별로 영화를 나누어 키워드에 맞는 영화를 제공하는 방식과 MBTI를 통한 추천 알고리즘으로 사용자의 성향에 맞는 영화를 제공하는 방식을 가진 서비스입니다.

현재까지 앞서 말한 서비스에 대한 프론트엔드와 백엔드 부분의 구현을 모두 마쳤습니다.

## 3. 데이터베이스 모델링 (ERD)

## 4. 영화 추천 알고리즘에 대한 기술적 설명

- 영화 추천 알고리즘은 모두 django를 통해 데이터 베이스에서 각 15개의 영화 객체를 중복없이 랜덤으로 가져와 리스트화하고 json화하여 Vue에 전송해주는 방식입니다.
- 랜덤 추천 기능은 데이터베이스에서 영화 객체를 랜덤으로 가져옵니다.
- MBTI별 추천 기능은 유저의 MBTI에 따른 보편적인 MBTI 별 선호 영화 장르에 따라 해당 장르의 영화 객체를 가져옵니다.
- 90년대 영화 추천 기능은 영화 데이터 중 released_date 컬럼의 앞자리가 199로 시작하는 영화 객체를 가져옵니다.
- 높은 평점의 영화 추천 기능은 영화 데이터 중 vote_average 컬럼이 높은 군에서 랜덤 영화 객체를 가져옵니다.

## 5. 서비스 대표 기능에 대한 설명

1. 영화 추천 기능 - 로그인한 사용자에게 사용자의 MBTI를 기반으로 추천 영화를 보여줍니다.
2. 영화 정보 제공 기능 - 사용자에게 다양한 키워드에 맞는 영화 정보(평점 , 줄거리)를 제공할 수 있습니다.
3. 위치기반 영화관 정보 제공 기능 - 사용자의 주변 또는 사용자가 검색한 지역의 주변 영화관을 조회할 수 있고 직접 지도에 마킹을 통해 위치를 알려줄 수 있습니다.
4. 회원가입 및 로그인 기능 - 사용자는 회원가입을 하여 로그인을 할 수 있습니다.
5. 커뮤니티 기능 - 사용자는 이미지를 포함해 글을 작성할 수 있으며 게시글에 좋아요를 하거나 게시글 작성자를 팔로잉하는 방식을 통해 다른 유저와 함께 커뮤니케이션을 할 수 있습니다.
6. 마이페이지, 프로필 기능 - 사용자의 정보, 커뮤니티에 작성한 글, 작성한 댓글을 조회할 수 있으며 팔로잉하고 팔로워한 사람들의 리스트를 볼 수 있습니다.

## 6. 느낀점, 후기

### 안대현

구상한 기능이나 디자인을 구현하는 데에 시행착오를 많이 겪으며 실력 부족을 많이 느꼈습니다. 그럼에도 기능이 의도된 대로 동작하게 하는 것을 성공했을 때의 재미와 즐거움이 컸습니다. 또한, 협업 시 소통과 의견조율의 중요성을 체감할 수 있었습니다. 더불어 프로젝트에 사용된 기술들에 대한 자신감도 키울 수 있어 보람도 느낄 수 있었습니다.

### 정진욱

Django와 Vue.js를 배우고 나서 처음으로 2가지를 같이 사용해 프로젝트를 만들어 보니 처음에 많은 어려움이 있었습니다. 하지만 Vue와 Django를 연결하는 부분에 점점 적응하게 되어 숙달될 수 있게 되었습니다.

다른 사람의 명세서를 통해 프로젝트를 만드는 방식이 아닌 직접 창작을 통해 프로젝트를 만들어야 했기에 준비와 기획을 잘해야 이후에 큰 어려움과 막힘 없이 프로젝트를 완성할 수 있다는 것을 깨닫게 되었습니다. 또한, 혼자가 함께 프로젝트를 할 때는 어떠한 부분을 신경을 써야 하는지 (코딩 컨벤션, git 사용)을 알게 되는 계기가 되었습니다.
