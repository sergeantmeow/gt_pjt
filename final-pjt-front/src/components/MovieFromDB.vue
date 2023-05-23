<template>
    <div>
        <h4 id="recommend_title">랜덤 추천 영화</h4>
        <div class="wrapper">
            <section id="section1">
            <a href="#section3" class="arrow__btn left-arrow">‹</a>
                <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[0].id)">
                    <div class="item">
                        <img
                        :src="`https://image.tmdb.org/t/p/w500/${movies[0]?.poster_path}`"
                        alt="Describe Image">
                        <h5 class="heading">{{ movies[0].title }}</h5>
                    </div>
                </div>
                <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[1].id)">
                    <div class="item">
                        <img
                        :src="`https://image.tmdb.org/t/p/w500/${movies[1]?.poster_path}`"
                        alt="Describe Image">
                        <h5 class="heading">{{ movies[1].title }}</h5>
                    </div>
                </div>
                <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[2].id)">
                    <div class="item">
                        <img
                        :src="`https://image.tmdb.org/t/p/w500/${movies[2]?.poster_path}`"
                        alt="Describe Image">
                        <h5 class="heading">{{ movies[2].title }}</h5>
                    </div>
                </div>
                <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[3].id)">
                    <div class="item">
                        <img
                        :src="`https://image.tmdb.org/t/p/w500/${movies[3]?.poster_path}`"
                        alt="Describe Image">
                        
                        <h5 class="heading">{{ movies[3].title }}</h5>
                    </div>
                </div>
                <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[4].id)">
                    <div class="item">
                        <img
                        :src="`https://image.tmdb.org/t/p/w500/${movies[4]?.poster_path}`"
                        alt="Describe Image">
                        <h5 class="heading">{{ movies[4].title }}</h5>
                    </div>
                </div>
            <a href="#section2" class="arrow__btn right-arrow">›</a>
            </section>

            <section id="section2">
            <a href="#section1" class="arrow__btn left-arrow">‹</a>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[5].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[5]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[5].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[6].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[6]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[6].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[7].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[7]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[7].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[8].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[8]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[8].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[9].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[9]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[9].title }}</h5>
                </div>
            </div>
            <a href="#section3" class="arrow__btn right-arrow">›</a>
            </section>

            <section id="section3">
            <a href="#section2" class="arrow__btn left-arrow">‹</a>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[10].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[10]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[10].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[11].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[11]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[11].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[12].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[12]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[12].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[13].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[13]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[13].title }}</h5>
                </div>
            </div>
            <div class="" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movies[14].id)">
                <div class="item">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[14]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[14].title }}</h5>
                </div>
            </div>
            <a href="#section1" class="arrow__btn right-arrow">›</a>
            </section>
        </div>

        <!-- Modal -->
    
        <div class="modal fade" id="movieModal" tabindex="-1" aria-labelledby="movieModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-fullsize">
              <img id="modal_bg_img" :src="`https://image.tmdb.org/t/p/w500/${this.$store.state.movie?.backdrop_path}`" alt="">
                <div class="modal-body bg-transparent container">
                    <div class="row">
                      <div class="col"><img id="modal_poster_img" :src="`https://image.tmdb.org/t/p/w500/${this.$store.state.movie?.poster_path}`" alt=""></div>
                      <div id="modal_content" class="col text-black">
                        <h3 class="modal-title fs-5 fw-bold" id="movieModalLabel">{{this.$store.state.movie?.title}}</h3>
                        <br>
                        <div v-if="showFullText">
                          <p>{{this.$store.state.movie?.overview}}</p>
                        </div>
                        <span v-else>
                          <span>{{ trimmedOverview }}</span>
                        </span>
                        <span v-if="showButton">
                          <button class="modal_btn" @click.stop="toggleText">{{ buttonText }}</button>
                        </span> 
                        <br>
                        <p style="margin-top: 10px;">개봉일: {{this.$store.state.movie?.release_date}}</p>
                        <div class="circle-wrap">
                          <div class="circle">
                            <div class="mask full">
                              <div class="fill"></div>
                            </div>
                            <div class="mask half">
                              <div class="fill"></div>
                            </div>
                            <div class="inside-circle"> {{ vote_num }}점 </div>
                          </div>
                        </div>
                      </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="modal_btn" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {

  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.movies,
      maxTextLength : 200,
      showFullText: false,
      vote_num : null,
    }
  },

  computed: {
    trimmedOverview(){
      if(this.$store.state.movie?.overview.length > this.maxTextLength){
        return this.$store.state.movie?.overview.slice(0, this.maxTextLength)+' ...'
      }else{
      // this.showFullText = true
      return this.$store.state.movie?.overview
      }
    },
    showButton(){
      return this.$store.state.movie?.overview.length > this.maxTextLength
    },
    buttonText(){
      return this.showFullText ? '숨기기' : '더보기'
    }
  },

  methods : {
    toggleText(){
      this.showFullText = !this.showFullText
    },
    async getMovie(pk){
        await this.$store.dispatch('getMovie', pk)
    },
  },
  watch : {
    '$store.state.movie':{
      handler(movie){
        if(movie.vote_average){
          let vote_num = parseFloat(this.$store.state.movie.vote_average) * 10
          let vote_degree = vote_num * 180 / 100
          let newAngle = vote_degree
          this.vote_num = vote_num
          let rotEle = document.querySelector('.circle-wrap .circle .mask.full' )
          let rotEle2 = document.querySelector('.circle-wrap .circle .fill')
          rotEle.style.transform = `rotate${vote_num}`
          rotEle2.style.transform = `rotate${vote_num}`

          // keyframes
          let keyframesRule = null;
          let styleSheets = document.styleSheets;

          for (let i = 0; i < styleSheets.length; i++) {
            var rules = styleSheets[i].cssRules || styleSheets[i].rules;
            for (let j = 0; j < rules.length; j++) {
              if (rules[j].type === CSSRule.KEYFRAMES_RULE && rules[j].name === 'fill') {
                keyframesRule = rules[j];
                break;
              }
            }
            if (keyframesRule) {
              break;
            }
          }
          if (keyframesRule) {
            var keyframesStyle = keyframesRule.cssRules || keyframesRule.rules;
            if (keyframesStyle.length === 2) {
              keyframesStyle[1].style.transform = 'rotate(' + newAngle + 'deg)';
            }
          }

        }
      },
      deep: true,
    }
  }
}

</script>

<style>
  :root{
    --font-size-md: calc(0.5rem + 2vw);
  }

  #recommend_title{
    margin-top: 15px;
    margin-bottom: 0;
    color: #bfbfbf;
  }
  #outerLine {
    margin: 14px
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    margin: 0;
    background-color: #000;
    font-family: Arial;
  }

  h1 {
    color: black;
    text-align: center;
  }

  .wrapper {
    display: grid;
    grid-template-columns: repeat(3, 100%);
    overflow: hidden;
    scroll-behavior: smooth;
  }
  .wrapper section {
    width: 100%;
    position: relative;
    display: grid;
    grid-template-columns: repeat(5, auto);
    margin: 20px 0;
  }
  .wrapper section .item {
    position: relative;
    padding: 0 2px;
    transition: 250ms all;
  }
  .wrapper section img{
    width: 100%;
  }
  .wrapper section .item:hover {
    margin: 0 40px;
    transform: scale(1.2);
  }
  .wrapper section .item .heading {
    position: absolute;
    bottom: 20px;
    color: black;
    opacity: 0;
    width: 100%;
    font-size: var(--font-size-md)
  }
  .wrapper section .item .heading:hover {
    position: absolute;
    bottom: 20px;
    color: black;
    font-weight: bold;
    background-color: rgba(255, 255, 255, 0.300);
    opacity: 1;
    width: 100%;
    font-size: var(--font-size-md)
  }
  .wrapper section img:hover ~ .heading {
    position: absolute;
    bottom: 20px;
    color: black;
    font-weight: bold;
    background-color: rgba(255, 255, 255, 0.300);
    opacity: 1;
    width: 100%;
    font-size: var(--font-size-md)
    
  }
  
  /* .wrapper section .item .duration {
    position: absolute;
    bottom: 0;
    left: 20px;
    color: #fff;
  } */
  .wrapper section .arrow__btn {
    position: absolute;
    color: #fff;
    text-decoration: none;
    font-size: 6em;
    background: black;
    width: 80px;
    padding: 20px;
    text-align: center;
    z-index: 1;
    display: flex;
    align-items: center;
  }
  .wrapper section .left-arrow {
    top: 0;
    bottom: 0;
    left: 0;
    background: transparent;
  }
  .wrapper section .left-arrow:hover {
    top: 0;
    bottom: 0;
    left: 0;
    background: linear-gradient(-90deg, rgba(0, 0, 0, 0) 0%, black 100%);
  }
  .wrapper section .right-arrow {
    top: 0;
    bottom: 0;
    right: 0;
    background: transparent;
  }
  .wrapper section .right-arrow:hover {
    top: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, black 100%);
  }

  #modal_bg_img{
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    /* overflow: auto; */
    object-fit: cover;
    z-index: -1;
    filter: contrast(20%);
    border-radius: 5px;
  }

  #modal_poster_img{
    width: 90%;
    align-content: left;
    border-radius: 4px;
    border: solid 2px #ff2679;
  }

  #modal_content{
    margin-right: 4%;
  }

  .modal_btn:hover{
    background-color: #352c41;;
    color: #ff9ec3;
  }

  .modal_btn {
    background-color: #261639;
    color: #ff2679;
    border: none;
    border-radius: 3px;
    z-index: 999;
    pointer-events: stroke;
  }

  .circle-wrap {
  margin: 50px auto;
  width: 150px;
  height: 150px;
  background: #e6e2e7;
  border-radius: 50%;
  }

  .circle-wrap .circle .mask,
  .circle-wrap .circle .fill {
    width: 150px;
    height: 150px;
    position: absolute;
    border-radius: 50%;
  }

  .circle-wrap .circle .mask {
    clip: rect(0px, 150px, 150px, 75px);
  }

  .circle-wrap .circle .mask .fill {
    clip: rect(0px, 75px, 150px, 0px);
    background-color: #ff2679;
  }

  .circle-wrap .circle .mask.full,
  .circle-wrap .circle .fill {
    animation: fill ease-in-out 1s;
    transform: rotate(10deg);
    animation-fill-mode: forwards;
  }

  @keyframes fill {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(150deg);
    }
  }

  .circle-wrap .inside-circle {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    background: #fff;
    line-height: 130px;
    text-align: center;
    margin-top: 10px;
    margin-left: 10px;
    position: absolute;
    z-index: 100;
    font-weight: 700;
    font-size: 2em;
  }


</style>