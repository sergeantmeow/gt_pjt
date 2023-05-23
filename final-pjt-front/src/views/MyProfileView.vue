<template>
  <div class="container">
    <h2 class="title-mg-ct mb-3">My Profile</h2>
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">이름: {{ currentUser.username }}</h5>
        <p class="card-text">MBTI: {{ currentUser.mbti }}</p>
        <p class="card-text">가입일: {{ formatDateTime(currentUser.date_joined) }}</p>
        <p class="card-text">최근 로그인: {{ formatDateTime(currentUser.last_login) }}</p>
        <router-link :to="{ name: 'MyProfileEditView' }" class="btn btn-primary">회원정보 수정</router-link>
      </div>
    </div>
    <hr>
    <UserFollowers :id="currentUser.id" />
    <hr>
    <UserFollowings :id="currentUser.id" />
    <hr>
    <UserArticle :username="currentUser.username" />
    <hr>
    <UserComment :username="currentUser.username" />
  </div>
</template>

<script>
import UserArticle from '@/components/UserArticle'
import UserComment from '@/components/UserComment'
import UserFollowers from '@/components/UserFollowers.vue'
import UserFollowings from '@/components/UserFollowings.vue'

export default {
  name: 'MyProfileView',
  components: {
    UserArticle, UserComment, UserFollowers, UserFollowings
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
      },
  },
  methods : {
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

.btn-primary:focus, .btn-primary.focus {
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
}
</style>