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
                        <p>{{this.$store.state.movie?.overview}}</p>
                        <br>
                        <p>평점: {{this.$store.state.movie?.vote_average}}</p> 
                        <br>
                        <p>개봉일: {{this.$store.state.movie?.release_date}}</p>
                        <p v-for="genre in this.$store.state.movie?.genre_ids" :key='genre.pk'>
                          {{genre.name}}
                        </p> 
                      </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="modal_close_btn" data-bs-dismiss="modal">Close</button>
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
      movies : this.$store.state.movies
    }
  },

  methods : {
    getMovie(pk){
        this.$store.dispatch('getMovie', pk)
    },
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
    overflow: auto;
    object-fit: cover;
    overflow: hidden;
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

  .modal_close_btn:hover{
    background-color: antiquewhite;
    color: gray
  }

  .modal_close_btn {
    background-color: #261639;
    color: #ff2679;
    border: none;
    border-radius: 3px;
  }


</style>