import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    movies: [
    ],
    cinemaMovies: [
    ],
    user: {
      token: null,
      username: null,
      mbti: null
    },
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // articles
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    // movies
    GET_MOVIES(state, movies){
      state.movies = movies
    },

    GET_MOVIES_CINEMA(state, cinemaMovies){
      state.cinemaMovies = cinemaMovies
      console.log('voila')
      console.log(cinemaMovies)
    },
    
    // accounts
    SET_USER(state, user) {
      state.user = user
    },

  },
  actions: {
    // movies
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then((response)=>{
        context.commit('GET_MOVIES', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    getMoviesCinema(context){
      const API_URL = 'http://api.themoviedb.org/3/movie/now_playing'
      axios({
        url: API_URL,
        params: {
          api_key : 'ce3376151cdca276068439ff358212cb',
          language : 'en-US',
          page : 1
        }
      })
      .then((response)=>{
        context.commit('GET_MOVIES_CINEMA', response.data.results)
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    // articles
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    // accounts
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const mbti = payload.mbti

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, mbti
        }
      })
        .then((res) => {
          const user = {
            token: res.data.key,
            username: username,
            mbti: mbti
          }
          context.commit('SET_USER', user)
          router.push({name: 'ArticleView'})
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        const user = {
          token: res.data.key,
          username: username,
          mbti: res.data.mbti
        }
        context.commit('SET_USER', user)
        router.push({name: 'ArticleView'})
      })
      .catch((err) => console.log(err))
    },
    logout(context){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.user.token}`
        }
      })
      .then(() => {
        context.commit('SAVE_TOKEN', null);
        context.commit('SAVE_USERNAME', null);
        context.commit('SAVE_MBTI', null);
        location.reload()
      })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
