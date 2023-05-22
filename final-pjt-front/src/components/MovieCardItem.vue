<template>
  <div class="col">
    <!-- <router-link :to="{
      name: 'MovieDetailView',
      params: { id: movieItem.id }}"> -->
      <div class="card" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movieItem.id)">
        <img id="posterID" :src="`https://image.tmdb.org/t/p/w500/${movieItem.poster_path}`" class="card-img-top" alt="">
        <!-- <div class="card-body">
          <h4 class="card-title fw-bold">{{ movieItem?.title }}</h4>
          <p>평점 평균 : {{ movieItem?.vote_average }}</p>
        </div> -->

      </div>
    <!-- </router-link> -->
  </div>
</template>

<script>
export default {
  name: 'MovieCardItem',
  props: {
    movieItem: Object,
  },
  methods : {
    getMovie(pk){
      this.$store.dispatch('getFilm', pk)
    }
  }
}
</script>

<style>
  .card:hover{
    transform: scale(1.1);
  }

</style>