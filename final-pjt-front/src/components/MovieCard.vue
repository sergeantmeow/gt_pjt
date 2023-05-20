<template>
  <div id="outerLine">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <!-- <MovieCardItem
      v-for="movieItem in movies"
      :key="movieItem.id"
      :movieItem="movieItem"
      class="col-md-4"
      /> -->
    </div>
    <MovieFromDB/>
    <MovieMBTI v-if="isLogin"/>
    <MovieRetro/>
    <MovieHigh/>
  </div>
  
</template>

<script>
import MovieFromDB from '@/components/MovieFromDB'
import MovieMBTI from '@/components/MovieMBTI'
import MovieRetro from '@/components/MovieRetro'
import MovieHigh from '@/components/MovieHigh'

export default {
  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.movies
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부 확인
    },
  },
  components: {
    MovieFromDB,
    MovieMBTI,
    MovieRetro,
    MovieHigh,
  },
}
</script>

<style>
  #outerLine {
    margin: 14px
  }

  
</style>