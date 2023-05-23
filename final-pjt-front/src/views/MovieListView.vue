<template>
  <div>
    <nav id="movie_navbar">
      <button class="movie_nav">
        <a href="" @click.prevent="popular" class="movie_menu text-decoration-none">Recommendations</a>
      </button>|
      <button class="movie_nav">
        <a href="" @click.prevent="cinema" class="movie_menu text-decoration-none">Now On Cinema</a>
      </button>|
      <button class="movie_nav">
        <a href="" @click.prevent="mbti" class="movie_menu text-decoration-none">Cinema Info</a>
      </button>
    </nav>
    <hr id="spacer">
    <div v-if="link === 1">
      <MovieCard/>
    </div>
    <div v-else-if="link === 2">
      <MovieOnCinema/>
    </div>
    <div v-else>
      <KakaoMap :options="mapOptions"/>
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
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부 확인
    },
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
    this.getUserGeo()
    this.getRetro()
    this.getHighRating()
    if(this.isLogin){
      this.getMBTI()
      // console.log('getmbti function initiated!')
    }
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
    },
    getMBTI(){
      this.$store.dispatch('getMBTIMovies')
    },
    getUserGeo(){
      this.$store.dispatch('getUserGeo')
    },
    getHighRating(){
      this.$store.dispatch('getHighRating')
    },
    getRetro(){
      this.$store.dispatch('getRetro')
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

.movie_nav{
  background-color: #261639;
  border-radius: 5px;
  border: none;
}
.movie_nav:hover{
  background-color: #352c41;
  border-radius: 5px;
  border: none;
}

.movie_menu{
  color: #ff2679
}
.movie_menu:hover{
  color: #ff9ec3;
}

</style>