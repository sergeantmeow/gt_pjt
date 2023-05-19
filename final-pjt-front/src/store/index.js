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
    mbtiMovies: [
    ],
    // user: {
    //   token: null,
    //   username: null,
    //   mbti: null,
    //   date_joined : null,
    //   last_login : null,
    // },
    user : {

    },
  },
  getters: {
    isLogin(state) {
      return state.user.token ? true : false
    },
    currentUser(state) {
      return state.user
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
    },

    GET_MBTI(state, mbtiMovies){
      state.mbtiMovies = mbtiMovies
    },
    
    // accounts
    SET_USER(state, user) {
      state.user = user
    },
    RESET_USER(state) {
      state.user = {}
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

    getMBTIMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/movies/mbti/`,
        params: {
          mbti : this.state.user.mbti
        }
      })
      .then((response)=>{
        context.commit('GET_MBTI', response.data)
      })
    },

    getMoviesCinema(context){
      const API_URL = 'http://api.themoviedb.org/3/movie/now_playing'
      axios({
        url: API_URL,
        params: {
          api_key : 'ce3376151cdca276068439ff358212cb',
          language : 'ko-KO',
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
      const { username, password1, password2, mbti } = payload;

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
            username,
            mbti
          }
          context.commit('SET_USER', user)
          context.dispatch('login', { username, password: password1 })
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
          username: res.data.user.username,
          mbti: res.data.user.mbti,
          date_joined : res.data.user.date_joined,
          last_login : res.data.user.last_login,
        }
        console.log(user)
        context.commit('SET_USER', user)
        router.push('/')
      })
      .catch((error) => {
        if (error.response && error.response.status === 400) {
          alert('잘못된 username 또는 password를 입력하셨습니다.')
        } else {
          console.log(error)
        }
      })
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
        context.commit('RESET_USER')
        localStorage.removeItem('vuex');
        // 이전 경로와 현재 경로가 다른 경우에만 이동
        if (router.history.current.path !== '/') {
          router.push('/');
          }
      })
      .catch((err) => console.log(err))
    },
  },
  modules: {
  }
})
