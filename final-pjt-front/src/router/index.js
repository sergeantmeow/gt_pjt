import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '../views/ArticleView'
import ArticleCreateView from '../views/ArticleCreateView'
import ArticleDetailView from '../views/ArticleDetailView'
import ArticleEditView from '../views/ArticleEditView'
import MovieListView from '@/views/MovieListView'
import MovieDetailView from '@/views/MovieDetailView'
import LogInView from '../views/LogInView'
import SignUpView from '../views/SignUpView'
import MyProfileView from '@/views/MyProfileView'
import OtherProfileView from '@/views/OtherProfileView'
import MyProfileEditView from '@/views/MyProfileEditView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView
  },

  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },

  {
    path: '/articles/detail/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },

  {
    path: '/articles/edit/:id',
    name: 'ArticleEditView',
    component: ArticleEditView
  },

  {
    path: '/MovieList',
    name: 'MovieListView',
    component: MovieListView
  },
  {
    path: '/MovieDetail',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView
  },

  {
    path: '/otherprofile/:username',
    name: 'OtherProfileView',
    component: OtherProfileView
  },

  {
    path: '/myprofile-edit',
    name: 'MyProfileEditView',
    component: MyProfileEditView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



export default router

