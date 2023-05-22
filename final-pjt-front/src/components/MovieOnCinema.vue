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
                        <h3 class="modal-title fs-7 fw-bold" id="movieModalLabel">{{this.$store.state.movie?.title}}</h3>
                        <br>
                        <p>{{this.$store.state.movie?.overview}}</p>
                        <br>
                        <p>평점: {{this.$store.state.movie?.vote_average}}</p> 
                        <br>
                        <p>개봉일: {{this.$store.state.movie?.release_date}}</p> 
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
import MovieCardItem from '@/components/MovieCardItem'
// import axios from 'axios'

export default {
  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.cinemaMovies,
      movieItem : this.$store.state.movie,
      moviesCarousel : null
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