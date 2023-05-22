<template>
  <div>
    <h1>MyProfile Page</h1>
    <p>이름: {{ currentUser.username }}</p>
    <p>MBTI: {{ currentUser.mbti }}</p>
    <p>가입일: {{ formatDateTime(currentUser.date_joined) }}</p>
    <p>최근 로그인: {{ formatDateTime(currentUser.last_login) }}</p>
    <router-link :to="{ name: 'MyProfileEditView' }">[회원정보 수정]</router-link>
    <hr>
    <UserArticle :username="currentUser.username" />
    <hr>
    <UserComment :username="currentUser.username" />
  </div>
</template>

<script>
import UserArticle from '@/components/UserArticle'
import UserComment from '@/components/UserComment'

export default {
  name: 'MyProfileView',
  components: {
    UserArticle, UserComment
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

<style>

</style>
