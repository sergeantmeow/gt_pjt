<template>
  <div class="col">
    <MovieCardItem
    v-for="movieItem in movies"
    :key="movieItem.id"
    :movieItem="movieItem"
    class="col-md-4"
    />
  </div>
</template>

<script>
import MovieCardItem from '@/components/MovieCardItem'
// import axios from 'axios'

export default {
  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.cinemaMovies
    }
  },
  components: {
    MovieCardItem,
  },
}
</script>

<style>
  #outerLine {
    margin: 14px
  }

</style>