<template>
  <div class="row row-cols-1 row-cols-md-4 g-4">
    <MovieCardItem
    v-for="movieItem in movies"
    :key="movieItem.id"
    :movieItem="movieItem"
    />
    <!-- Modal -->
    <div class="modal fade" id="movieModal" tabindex="-1" aria-labelledby="movieModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-fullsize">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="movieModalLabel">{{this.$store.state.movieItem?.title}}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <img :src="`https://image.tmdb.org/t/p/w500/${this.$store.state.movie?.poster_path}`" alt="">
                <br>
                내용: {{this.$store.state.movie?.overview}}
                <br>
                평점: {{this.$store.state.movie?.popularity}}
                <br>
                개봉일: {{this.$store.state.movie?.release_date}}
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
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
      movieItem : this.$store.state.movie
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