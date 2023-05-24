<template>
  <div>
    <h1>Movie Detail Block</h1>
    <p>{{ movie?.title }}</p>
    <p>{{ movie?.overview }}</p>
  </div>
</template>

<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  data(){
    return { 
      movie: null
    }
  },
  created(){
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail(){
      const API_URL = 'https://api.themoviedb.org/3/movie'
      axios({
        url: `${API_URL}/${this.$route.params.id}`,
        params: {
          api_key : 'ce3376151cdca276068439ff358212cb',
          language : 'ko-KO',

        }
      })
      .then((response)=>{
        this.movie = response.data
      })
      .catch((err)=>{
        console.log(err)
        console.log(this.$route.params.id)
        console.log('error! error!')
      })
    }
  }
}
</script>

<style>

</style>