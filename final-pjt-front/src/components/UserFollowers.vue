<template>
  <div>
    <h3 @click="toggleFollowers" class="follower-title">팔로워</h3>
    <ul v-if="showFollowers" class="list-group">
      <li v-for="follower in followers" :key="follower.id" class="list-group-item">
        <router-link :to="{ name: 'OtherProfileView',
         params: { username: follower.username } }"
          class="item">
          {{ follower.username }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'UserFollowers',
  data() {
    return {
      followers: [],
      showFollowers: false,
    }
  },
  props: {
    id: Number,
  },
  created() {
    this.getFollowers();
  },
  methods: {
    toggleFollowers() {
      if (this.showFollowers) {
        this.showFollowers = false;
      } else {
        this.getFollowers();
      }
    },
    getFollowers() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/${this.id}/followers/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        }
      })
      .then((response) => {
        this.followers = response.data;
        this.showFollowers = true;
      })
      .catch((error) => {
        console.error(error);
      });
    }
  },
}
</script>

<style scoped>
.follower-title {
  transition: transform 0.3s ease;
}
.follower-title:hover {
  transform: scale(1.1);
}

.list-group-item {
  border-color: rgb(31, 32, 63, 0);
  background-color: rgb(31, 32, 63, 0);
  color: #bfbfbf;
}

.list-group-item:hover {
  background-color: rgba(79, 61, 99, 0);
  color: #ff2679;
}

.item {
  color: #bfbfbf;
  text-decoration : none;
}

.item:hover {
  color: #ff2679
}

</style>