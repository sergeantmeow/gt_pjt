import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
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
import HomeView from '@/views/HomeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView,
  },

  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView,
    meta: {
      requiresAuth: true
    }
  },

  {
    path: '/articles/detail/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
  },

  {
    path: '/articles/edit/:id',
    name: 'ArticleEditView',
    component: ArticleEditView,
    meta: {
      requiresAuth: true
    }
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
    component: MyProfileView,
    meta: {
      requiresAuth: true
    }
  },

  {
    path: '/otherprofile/:username',
    name: 'OtherProfileView',
    component: OtherProfileView,
    meta: {
      requiresAuth: true
    }
  },

  {
    path: '/myprofile-edit',
    name: 'MyProfileEditView',
    component: MyProfileEditView,
    meta: {
      requiresAuth: true
    }
  },
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !store.getters.isLogin) {
    next('/login'); 
  } else {
    next();
  }
});



export default router

