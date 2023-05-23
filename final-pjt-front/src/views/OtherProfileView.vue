<template>
  <div class="container" v-if="user">
    <h2 class="title-mg-ct mb-3" >{{ user.username }} Profile</h2>
    <div class="card mb-4">
      <div class="card-body">
        <template v-if="user">
          <p class="card-title">이름: {{ user.username }}</p>
          <p class="card-text">MBTI: {{ user.mbti }}</p>
          <p class="card-text">가입일: {{ formatDateTime(user.date_joined) }}</p>
          <p class="card-text">최근 로그인: {{ formatDateTime(user.last_login) }}</p>
          <p>팔로워 : {{ user.followers.length }}</p>
          <div v-if="isNotAuthor">
            <button @click="followUser" class="btn btn-primary">팔로잉</button>   
          </div>  
        </template>
      </div>
    </div>
    <hr>
    <UserFollowers :id="user.id" />
    <hr>
    <UserFollowings :id="user.id" />
    <hr>
    <UserArticle :username="user.username" />
    <hr>
    <UserComment :username="user.username" />
  </div>
</template>

<script>
import axios from 'axios'
import UserArticle from '@/components/UserArticle'
import UserComment from '@/components/UserComment'
import UserFollowers from '@/components/UserFollowers.vue'
import UserFollowings from '@/components/UserFollowings.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OtherProfileView',
  components: {
    UserArticle, UserComment, UserFollowers, UserFollowings
  },
  data() {
    return {
      user : null
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    currentUser(){
      return this.$store.getters.currentUser
    },
    isNotAuthor() {
      return this.isLogin && this.user?.username != this.currentUser.username
    },
  },
  created(){
      this.getUserProfile(this.$route.params.username);
  },
  methods: {
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    getUserProfile(username) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${username}/`,
      })
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    },
    followUser() {
      const id = this.user.id
      axios({
        method: 'post',
        url: `${API_URL}/accounts/follow/${id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        this.getUserProfile(this.$route.params.username);
      })
      .catch((error) => {
        console.log(error);
      });
    },
  }
};
</script>

<style scoped>
.card {
  width: 100%;
  background-color: rgb(31, 32, 63);
  border-color: rgb(31, 32, 63);
  color: #bfbfbf;
}

.btn-primary {
  color: #bfbfbf;
  background-color: #4f3d63;
  border-color: #4f3d63;
}

.btn-primary:hover {
  color: #ff2679;
  background-color: #4f3d63;
  border-color: #4f3d63;
}
</style>