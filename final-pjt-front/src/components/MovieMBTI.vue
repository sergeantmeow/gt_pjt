<template>
    <div>
        <h4 id="recommend_title">{{mbti}}인 당신에게 맞는 추천 영화</h4>
        <div class="wrapper">
            <section id="section4">
            <a href="#section6" class="arrow__btn left-arrow">‹</a>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[0].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[0]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[0]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[1].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[1]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[1]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[2].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[2]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[2]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[3].id }}">
                <div class="item1">
                    <img
                    :src="`https://image.tmdb.org/t/p/w500/${movies[3]?.poster_path}`"
                    alt="Describe Image">
                    <h5 class="heading">{{ movies[3]?.title }}</h5>
                </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[4].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[4]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[4]?.title }}</h5>
              </div>
            </router-link>
            <a href="#section5" class="arrow__btn right-arrow">›</a>
            </section>

            <section id="section5">
            <a href="#section4" class="arrow__btn left-arrow">‹</a>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[5].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[5]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[5]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[6].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[6]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[6]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[7].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[7]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[7]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[8].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[8]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[8]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[9].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[9]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[9]?.title }}</h5>
              </div>
            </router-link>
            <a href="#section6" class="arrow__btn right-arrow">›</a>
            </section>

            <section id="section6">
            <a href="#section5" class="arrow__btn left-arrow">‹</a>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[10].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[10]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[10]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[11].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[11]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[11]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[12].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[12]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[12]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[13].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[13]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[13]?.title }}</h5>
              </div>
            </router-link>
            <router-link :to="{
                 name: 'MovieDetailView',
                 params: { id: movies[14].id }}">
              <div class="item1">
                  <img
                  :src="`https://image.tmdb.org/t/p/w500/${movies[14]?.poster_path}`"
                  alt="Describe Image">
                  <h5 class="heading">{{ movies[14]?.title }}</h5>
              </div>
            </router-link>
            <a href="#section4" class="arrow__btn right-arrow">›</a>
            </section>
        </div>
    </div>
</template>

<script>
export default {

  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.mbtiMovies,
      mbti : this.$store.state.user.mbti
    }
  },
}

</script>

<style>
  :root{
    --font-size-md: calc(0.5rem + 2vw);
  }
  #recommend_title{
    margin-top: 20px;
    margin-bottom: 0;
    color: white;
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
    color: red;
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
  .wrapper section .item1 {
    position: relative;
    padding: 0 2px;
    transition: 250ms all;
  }
  .wrapper section img{
    width: 100%;
  }
  .wrapper section .item1:hover {
    margin: 0 40px;
    transform: scale(1.2);
  }
  .wrapper section .item1 .heading {
    position: absolute;
    bottom: 20px;
    color: black;
    opacity: 0;
    width: 100%;
    font-size: var(--font-size-md)
  }
  .wrapper section .item1 .heading:hover {
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
  
  /* .wrapper section .item1 .duration {
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
</style>