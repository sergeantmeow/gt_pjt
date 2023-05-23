<template>
  <div>
    <h3 id="top3">상영 중인 영화 TOP3</h3>
    <div id="carousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="3000">
          <img :src="`https://image.tmdb.org/t/p/original/${moviesCarousel[0].backdrop_path}`" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>{{moviesCarousel[0].title}}</h5>
            <p>평점: {{moviesCarousel[0].vote_average}}</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img :src="`https://image.tmdb.org/t/p/original/${moviesCarousel[1].backdrop_path}`" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>{{moviesCarousel[1].title}}</h5>
            <p>평점: {{moviesCarousel[1].vote_average}}</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img :src="`https://image.tmdb.org/t/p/original/${moviesCarousel[2].backdrop_path}`" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>{{moviesCarousel[2].title}}</h5>
            <p>평점: {{moviesCarousel[2].vote_average}}</p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <div class="row row-cols-1 row-cols-md-4 g-4">
      <MovieCardItem
      v-for="movieItem in movies"
      :key="movieItem.id"
      :movieItem="movieItem"
      />
    </div>
    <!-- Modal -->
    
        <div class="modal fade" id="movieModal" tabindex="-1" aria-labelledby="movieModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-fullsize">
              <img id="modal_bg_img" :src="`https://image.tmdb.org/t/p/w500/${this.$store.state.movie?.backdrop_path}`" alt="">
                <div class="modal-body bg-transparent container">
                    <div class="row">
                      <div class="col"><img id="modal_poster_img" :src="`https://image.tmdb.org/t/p/w500/${this.$store.state.movie?.poster_path}`" alt=""></div>
                      <div id="modal_content" class="col text-black fw-bold">
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
                        <div class="row">
                          <div class="col">
                            <ul>
                              <li>
                              </li>
                            </ul>
                            원제 : {{ this.$store.state.movie?.original_title }}
                          </div>
                          <div class="col">
                            평점 평균
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
import MovieCardItem from '@/components/MovieCardItem'
// import axios from 'axios'

export default {
  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.cinemaMovies,
      movieItem : this.$store.state.movie,
      moviesCarousel : null,
      maxTextLength : 300,
      showFullText: false,
      vote_num : null,
    }
  },
  computed: {
    trimmedOverview(){
      console.log(this.$store.state.movie?.overview.length)
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
  components: {
    MovieCardItem,
  },
  created(){
  const popFilms = []
  const films = this.$store.state.cinemaMovies
  let filmsByRate
  filmsByRate = films.sort((a,b)=> b.vote_average - a.vote_average)
  for(let i=0; i<3; i++){
    popFilms.push(filmsByRate[i])
  }
  this.moviesCarousel = popFilms
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
          this.vote_num = parseInt(vote_num)
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
  #outerLine {
    margin: 14px
  }

  #carousel{
    margin-top: 20px;
    margin-bottom: 20px;
  }

  #top3{
    color: white
  }


</style>