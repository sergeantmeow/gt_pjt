<template>
  <div>
    <nav id="movie_navbar">
      <!-- <router-link :to="{ name: 'MovieListView'}">인기작</router-link> |
      <router-link :to="{ name: 'MovieOnCinema' }">지금 상영 중</router-link> |
      <router-link :to="{ name: 'ArticleView' }">맞춤 추천</router-link> -->
      <button class="btn btn-warning">
        <a href="" @click.prevent="popular" class="text-decoration-none fw-bold">Recommendations</a>
      </button>|
      <button class="btn btn-warning">
        <a href="" @click.prevent="cinema" class="text-decoration-none fw-bold">Now On Cinema</a>
      </button>|
      <button class="btn btn-warning">
        <a href="" @click.prevent="mbti" class="text-decoration-none fw-bold">To Be Added</a>
      </button>
    </nav>
    <hr id="spacer">
    <div v-if="link === 1">
      <MovieCard/>
    </div>
    <div v-else-if="link === 2">
      <KakaoMap :options="mapOptions"/>
      <MovieOnCinema/>
    </div>
    <div v-else>
      <p>맞춤 추천은 이 곳</p>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MovieOnCinema from '@/components/MovieOnCinema'
import KakaoMap from '@/components/KakaoMap.vue'

export default {
  name: 'MovieListView',
  components: {
    MovieCard,
    MovieOnCinema,
    KakaoMap,
  },
  data(){
    return{
      link : 1,
      mapOptions:{
        center: {
          lat: 36.107169,
          lng: 128.41622,
        },
        level: 5
      }
    }
  },
  created(){
    this.getLink()
    this.getCine()
  },
  methods : {
    popular(){
      this.link = 1
    },
    cinema(){
      this.link = 2
    },
    mbti(){
      this.link = 3
    },
    getLink(){
      this.$store.dispatch('getMovies')
    },
    getCine(){
      this.$store.dispatch('getMoviesCinema')
    }
  },

}
</script>

<style>
#spacer {
  margin: none
}
#movie_navbar{
  margin-top: 1rem;
}

</style>