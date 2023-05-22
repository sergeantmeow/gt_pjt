<template>
  <div class="col">
      <div class="card" data-bs-toggle="modal" data-bs-target="#movieModal" @click="getMovie(movieItem.id)">
        <img id="posterID" :src="`https://image.tmdb.org/t/p/w500/${movieItem.poster_path}`" class="card-img-top" alt="">
      </div>
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

  .card{
    border: solid 2px #7c6891
  }

</style>