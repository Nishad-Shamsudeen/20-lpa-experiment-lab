import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const useUserList = ()=>{
    return useQuery({
    queryKey: ["users"],
    queryFn: async () => {
      const response = await axios(
        `${API_URL}/users`
      );
       return response.data;
    },
      //USED TO CONTROLL AUTO FETCH
    refetchOnWindowFocus: false, // Stop unnecessary Refetch API After Window focus
  });
}

export const useUserListMutation=()=>{
const query = useQueryClient();
    return useMutation({
    mutationFn: async () => {
      const response = await axios(
        `${API_URL}/users`,
        {
          method: "POST",
          data: {
            id: "testNsdID",
            name: "TestNsd",
          },
        }
      );
      return response.data;
    },
    //Data after mutation
    onSuccess: (data) => {
      query.invalidateQueries({
        queryKey: ["users"],
      });
    },
  });
}