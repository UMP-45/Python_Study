function x=gauss_column(A,b)  	%�������A��������b�����ؽ�����x
[ni,nj]=size(b);
if rank(A)~=rank([A,b])				%��ϵ�������Ⱥ���������Ȳ���ȣ����޽�
    fprintf('�޽�\n')
    return
else if rank(A)<ni							%��ϵ�������Ⱥ������������ȣ���������С��δ֪���������������
        fprintf('�����\n')
        return
    else
        for j=1:ni
            [tv,ti]=max(A(j:ni,j));			%�ҳ������а�ģ����Ԫ��
            A([ti+j-1,j],:)=A([j,ti+j-1],:);%������
            for i=j+1:ni						%��ȥ����
                d=-A(i,j)/A(j,j);
                A(i,:)=A(i,:)+d*A(j,:);
                b(i)=b(i)+d*b(j);
            end
        end
        x=zeros(size(b));					%��ʼ��������
        x(ni)=b(ni)/A(ni,ni);
        for i=ni-1:-1:1						%�ش�����
            x(i)=(b(i)-sum(x.*A(i,:)'))/A(i,i);
        end
    end
end