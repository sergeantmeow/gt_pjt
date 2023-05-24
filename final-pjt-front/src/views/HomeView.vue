<template>
  <div id="main_introduction">
    
    <a id="languageSet" class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
      Language
    </a>
    <ul id="languager_dropdown" class="dropdown-menu">
      <li><a class="dropdown-item" href="#" @click="setKorean"><img src="../assets/korflag.png" alt=""> 한국어</a></li>
      <li><a class="dropdown-item" href="#" @click="setEnglish"><img src="../assets/usflag.png" alt=""> English</a></li>
      <li><a class="dropdown-item" href="#" @click="setFrench"><img src="../assets/frflag.png" alt=""> Français</a></li>
    </ul>
    <img src="../assets/lettering2.png" style="margin-bottom: 6px;" alt="">
    <div class="row">
        <div id="intro_textBox" class="col">
            <div v-if="language === 'english'">
                Sweet 1990's.
                The time when people didn't look into the tiny screens on their palms. The time when custom were over law, and violent were over manners.
                Optimism was quite a thing with the economic growth which seemed to last forever. 
                <br>
                For those who miss the VCR rental, 16 bit video game console, local general store,
                cheesy noir films, and leon lights filling the night air, Some Like It 90's introduces 90's theme online film community. You can look for film commendations by your MBTI,
                film rating, and by the year they were released. It show features movies on cinema now as well as the cinema location informations. Not to mention there is a board where
                you can share your opinions and informations to. Grab your mouse, and probably pop-corn too, enjoy the 90's!
            </div>
            <div v-if="language === 'korean'">
                90년대. 사람들이 손 위의 작은 화면을 들여다보지 않던 때죠. 법보다는 관습이, 매너보다는 폭력이 먼저였던 때이기도 합니다. 
                영원할 것 같던 경제성장으로 낙관주의가 팽배했구요. 
                <br>
                비디오 렌탈, 16비트 게임기, 동네 문방구, 오그라드는 느와르 영화, 
                그리고 밤공기를 채우던 네온사인 불빛들을 그리워하는 이들을 위해 Some Like It 90's는 90년대 테마의 온라인 영화 커뮤니티를 소개합니다.
                사용자의 MBTI, 평점, 그리고 개봉 연도를 기반으로한 영화 추천 기능과 더불어 영화의 위치정보와 함께 현재 상영 중인 영화도 둘러볼 수 있습니다.
                의견과 정보를 공유할 게시판도 물론 있고 말이죠. 이제 마우스와 팝콘을 잡고 90년대를 즐기세요!
            </div>
            <div v-if="language === 'french'">
                Chères années 90,
                Temps où les gens ne restaient pas fixés à de petits écrans collés sur leur main.
                Temps où la coutume l'emportait sur la loi, et la violence sur les manières.
                Temps où l'optimisme était au rendez-vous avec une croissance économique qui semblait durer éternellement.
                À ceux à qui la location de K7, les consoles 16 bits, les magasins de quartier, les films mielleux et les néons lumineux manquent.
                Vous pouvez rechercher des films en fonction de votre MBTI, de leur classement et de leur année de sortie. Vous trouverez des informations sur les films actuellement au cinéma ainsi que sur la localisation des cinémas qui les diffusent.
                Vous pourrez également y trouver un emplacement où partager vos avis ou toutes autres informations qui vous semblent utiles.
                Alors attrapez votre souris et pourquoi pas quelques pop-corns et profitez des années 90 !
            </div>
        </div>
        <div class="col">
            <img id="introduction_img" src="../assets/cinema2.jpg" alt="">
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data(){
    return{
        language: 'korean'
    }
  },
  methods : {
    setEnglish(){
        this.language = 'english'
    },
    setKorean(){
        this.language = 'korean'
    },
    setFrench(){
        this.language = 'french'
    }
  }
}
</script>

<style>
    #languageSet{
        text-align: left;
        margin-left: 16px;
    }

    #main_introduction{
        background-image: url("../assets/main_background_2.jpg");
        width : 100%;
        background-size: cover;
        color : #261639;
        font-weight: bold;
    }
    #introduction_img{
        width: 90%;
        margin-bottom: 16px;
        border: solid 3px rgb(109, 14, 109);
        border-radius: 4px;
    }
    #intro_textBox{
        /* border: solid 2px black; */
        margin-bottom: 16px;
        margin-left: 16px;
        text-align: left;
    }
    #languager_dropdown{
        background-color: #261639;
    }
    .dropdown-item{
        color: #ff2679;
    }
    
    
</style>