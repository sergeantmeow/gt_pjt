<template>
  <div>
    <h1>MyProfile Page</h1>
    <p>이름: {{ currentUser.username }}</p>
    <p>MBTI: {{ currentUser.mbti }}</p>
    <p>가입일: {{ currentUser.date_joined }}</p>
    <p>최근 로그인: {{ currentUser.last_login }}</p>
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
  };
</script>

<style>

</style>
