<template>
  <div>
    <h1>MyProfile Page</h1>
    <p>사용자 이름: {{ currentUser.username }}</p>
    <p>사용자 MBTI: {{ currentUser.mbti }}</p>
    <p>가입일: {{ currentUser.date_joined }}</p>
    <p>최근 로그인: {{ currentUser.last_login }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyProfileView',
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
      },
    },
  };
</script>

<style>

</style>
