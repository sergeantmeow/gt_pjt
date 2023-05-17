<template>
  <div id="outerLine">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MovieCardItem
      v-for="movieItem in movies"
      :key="movieItem.id"
      :movieItem="movieItem"
      class="col-md-4"
      />
    </div>
  </div>
</template>

<script>
import MovieCardItem from '@/components/MovieCardItem'

export default {
  name: 'MovieCard',
  data(){
    return {
      movies : this.$store.state.movies
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